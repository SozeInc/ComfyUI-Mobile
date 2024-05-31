import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";

class FlowState {
    constructor(){}
    static idle() {
        return (!app.runningNodeId);
    }
    static paused() {
        if (app.runningNodeId)
            return (app.graph?._nodes_by_id[app.runningNodeId.toString()]?.comfyClass === "Settings Launcher (Mobile)");
        return false;
    }
    static paused_here(node_id) {
        return (FlowState.paused() && FlowState.here(node_id))
    }
    static running() {
        return (!FlowState.idle());
    }
    static here(node_id) {
        return (app.runningNodeId==node_id);
    }
    static state() {
        if (FlowState.paused()) return "Paused";
        if (FlowState.running()) return "Running";
        return "Idle";
    }
    static cancelling = false;
}
function send_proceed() {
    const body = new FormData();
    api.fetchApi("/settings_launcher_flow_control_proceed", { method: "POST"});
}
function send_cancel() {
    const body = new FormData();
    api.fetchApi("/settings_launcher_flow_control_cancel", { method: "POST"});
}



function progressButtonPressed() {
    const node = app.graph._nodes_by_id[this.node_id];
    console.log("[ComfyMobile][progressButtonPressed] FlowState: " + FlowState.state() + " this.name: " + this.name);
    if (this.name!='') {
        if (FlowState.paused()) {
            send_proceed();
        }
    }
}

function cancelButtonPressed() { 
    console.log("[ComfyMobile][cancelButtonPressed] FlowState: " + FlowState.state())
    if (FlowState.running()) { send_cancel(); } 
}

/*
Comfy uses 'clicked' to make the button flash; so just disable that.
This *doesn't* stop the callback, it's totally cosmetic!
*/
function enable_disabling(button) {
    Object.defineProperty(button, 'clicked', {
        get : function() { return this._clicked; },
        set : function(v) { this._clicked = (v && this.name!=''); }
    })
}

function disable_serialize(widget) {
    if (!widget.options) widget.options = {  };
    widget.options.serialize = false;
}

app.registerExtension({
    name: "mobilenodes.settings_launcher",
    init() {
        window.addEventListener("beforeunload", send_cancel, true);
    },
    setup() {
        console.log("[ComfyMobile][setup]")
        /*
        If a run is interrupted, send a cancel message (unless we're doing the cancelling, to avoid infinite loop)
        */
        const original_api_interrupt = api.interrupt;
        api.interrupt = function () {
            console.log("[ComfyMobile][api.interrupt] Flow.state: " + FlowState.state())
            if (FlowState.paused() && !FlowState.cancelling) send_cancel();
            original_api_interrupt.apply(this, arguments);
        }

        /*
        Cancel-on-Queue
        */
        function on_execution_interrupted() {
            console.log("[ComfyMobile][on_execution_interrupted] FlowState: " + FlowState.state());
            if (FlowState.paused()) send_cancel();
        }

        function intercept_queue_triggers() {
            console.log("[ComfyMobile][intercept_queue_triggers] FlowState: " + FlowState.state());
            if (FlowState.paused()) api.interrupt();
        }

        api.addEventListener("execution_interrupted", on_execution_interrupted);

        document.getElementById("queue-button").addEventListener("click", intercept_queue_triggers);
        document.addEventListener("keydown", function (event) {
            if (event.key == "Enter" && event.ctrlKey) {
                intercept_queue_triggers();
            }
        })
    },

    async nodeCreated(node) {
        try
        {
            if (node?.comfyClass === "Settings Launcher (Mobile)") {
                console.log("[ComfyMobile][nodeCreated]" + node?.comfyClass)
                /* Capture clicks */
                const org_onMouseDown = node.onMouseDown;
                node.onMouseDown = function( e, pos, canvas ) {
                    return (org_onMouseDown && org_onMouseDown.apply(this, arguments));
                }

                /* The buttons */
                node.send_button_widget = node.addWidget("button", "", "", progressButtonPressed);
                node.cancel_button_widget = node.addWidget("button", "", "", cancelButtonPressed);
                enable_disabling(node.cancel_button_widget);
                enable_disabling(node.send_button_widget);
                disable_serialize(node.cancel_button_widget);
                disable_serialize(node.send_button_widget);
            }
        } catch (e) {
            console.error("[ComfyMobile][nodeCreated]" + e);
        }
    },
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        try
        {
            if (nodeType?.comfyClass==="Settings Launcher (Mobile)") {
                console.log("[ComfyMobile][beforeRegisterNodeDef] FlowState: " + FlowState.state())
                /* Update the node when the flow state changes - change button labels */
                const update = nodeType.prototype.update;
                nodeType.prototype.update = function() {
                    if (update) update.apply(this,arguments);
                    if (this.send_button_widget) {
                        this.send_button_widget.node_id = this.id;

                        if (FlowState.paused_here(this.id)) {
                            this.send_button_widget.name ="Proceed";
                        } else {
                            this.send_button_widget.name = "";
                        }
                    }
                    if (this.cancel_button_widget) this.cancel_button_widget.name = FlowState.running() ? "Cancel" : "";
                    this.setDirtyCanvas(true,true); 
                }
            }
        } catch (e) {
            console.error("[ComfyMobile][beforeRegisterNodeDef]" + e);
        }
    },
});

