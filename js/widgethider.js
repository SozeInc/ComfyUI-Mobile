import { app } from "../../scripts/app.js";

let initialized = false;
let origProps = {};

const findWidgetByName = (node, name) => {
    return node.widgets ? node.widgets.find((w) => w.name === name) : null;
};

const findInputByName = (node, name) => {
    return node.inputs ? node.inputs.find((w) => w.name === name) : null;
};
const doesInputWithNameExist = (node, name) => {
    return node.inputs ? node.inputs.some((input) => input.name === name) : false;
};

function widgetLogic(node, widget) {
    // Retrieve the handler for the current node title and widget name
    if (widget.name == "concat_count") {
        handleSozeUltimateConcatCount(node, widget);
    } 
    //else if (String(widget.name).slice(0,7) == "prefix_") {
    //    const idx = parseInt(String(widget.name).slice(7));
    //    handleSozeUltimateConcatInputRename(node, idx);
    //}
}

function handleSozeUltimateConcatInputRename(node, idx) {
    try
    {
        const concatCountWidget = findWidgetByName(node, "concat_count");
        if (idx <= concatCountWidget.value) {
            const prefixWidget = findWidgetByName(node, `prefix_${idx}`);
            const valueWidget = findInputByName(node, `value_${idx}`);
            if (prefixWidget.value != "") valueWidget.name = `${prefixWidget.value}_value_${idx}`;
        }
    } catch (e) {
        console.error("[SOZE][handleSozeUltimateConcatInputRename]" + e);
    }
}

function handleSozeUltimateConcatCount(node, widget) {
    try
    {
        const countValue = widget.value;
        for (let i = 1; i <= 24; i++) {
            const prefixWidget = findWidgetByName(node, `prefix_${i}`);
            const valueWidget = findInputByName(node, `value_${i}`);
            if(i <= countValue) {
                toggleWidget(node, prefixWidget, true);
                toggleWidget(node, valueWidget, true);  
            }else{
                toggleWidget(node, prefixWidget, false);
                toggleWidget(node, valueWidget, false);
            }
        }
    } catch (e) {
        console.error("[SOZE][handleSozeUltimateConcatCount]" + e);
    }
}

const HIDDEN_TAG = "tschide";

// Toggle Widget + change size
function toggleWidget(node, widget, show = false, suffix = "") {
    try
    {
        // If the widget doesn't exist or the input with the same name exists, return
        if (!widget || doesInputWithNameExist(node, widget.name)) {
            return;
        }

        // Store the original properties of the widget if not already stored
        if (!origProps[widget.name]) {
            origProps[widget.name] = { origType: widget.type, origComputeSize: widget.computeSize };
        }

        const origSize = node.size;

        // Set the widget type and computeSize based on the show flag
        widget.type = show ? origProps[widget.name].origType : HIDDEN_TAG + suffix;
        widget.computeSize = show ? origProps[widget.name].origComputeSize : () => [0, -4];

        // Recursively handle linked widgets if they exist
        widget.linkedWidgets?.forEach(w => toggleWidget(node, w, ":" + widget.name, show));

        // Calculate the new height for the node based on its computeSize method
        const newHeight = node.computeSize()[1];
        node.setSize([node.size[0], newHeight]);
    } catch (e) {
        console.error("[SOZE][toggleWidget]" + e);
    }
}

app.registerExtension({
    name: "sozenodes.widgethider",
    nodeCreated(node) {
        for (const w of node.widgets || []) {
            let widgetValue = w.value;
            // Store the original descriptor if it exists
            let originalDescriptor = Object.getOwnPropertyDescriptor(w, 'value');

            widgetLogic(node, w);

            Object.defineProperty(w, 'value', {
                get() {
                    // If there's an original getter, use it. Otherwise, return widgetValue.
                    let valueToReturn = originalDescriptor && originalDescriptor.get
                        ? originalDescriptor.get.call(w)
                        : widgetValue;

                    return valueToReturn;
                },
                set(newVal) {

                    // If there's an original setter, use it. Otherwise, set widgetValue.
                    if (originalDescriptor && originalDescriptor.set) {
                        originalDescriptor.set.call(w, newVal);
                    } else {
                        widgetValue = newVal;
                    }
                    widgetLogic(node, w);
                }
            });
        }
        setTimeout(() => {initialized = true;}, 500);
    }
});