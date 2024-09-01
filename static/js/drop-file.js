document.addEventListener("DOMContentLoaded", function () {
    const dropZone = document.getElementById("dropZone");
    const selectedFileName = document.getElementById('selectedFileName');
    const fileInput = document.getElementById("id_archivo");
    const fileError = document.getElementById("fileError");
    const allowedTypes = [
        "image/png",
        "image/jpeg",
        "image/gif",
        "application/pdf",
        "text/csv",
    ];

    ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ["dragenter", "dragover"].forEach((eventName) => {
        dropZone.addEventListener(eventName, highlight, false);
    });

    ["dragleave", "drop"].forEach((eventName) => {
        dropZone.addEventListener(eventName, unhighlight, false);
    });

    function highlight() {
        dropZone.classList.add("border-primary", "bg-gray-50");
    }

    function unhighlight() {
        dropZone.classList.remove("border-primary", "bg-gray-50");
    }

    dropZone.addEventListener("drop", handleDrop, false);
    dropZone.addEventListener("click", () => fileInput.click());
    fileInput.addEventListener("change", handleFileSelect);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
    }

    function handleFileSelect(e) {
        const files = e.target.files;
        handleFiles(files);
    }

    function handleFiles(files) {
        if (files.length > 0) {
            const file = files[0];
            if (allowedTypes.includes(file.type)) {
                fileInput.files = files;
                updateFileName(file.name);
                fileError.classList.add("hidden");
            } else {
                fileInput.value = "";
                updateFileName("");
                fileError.classList.remove("hidden");
            }
        }
        unhighlight();
    }
    function updateFileName(name) {
        selectedFileName.textContent = name ? `Archivo seleccionado: ${name}` : '';
    }
});
