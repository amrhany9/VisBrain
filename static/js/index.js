document.addEventListener("DOMContentLoaded", function () {
    const uploadButton = document.getElementById("upload-button");
    const testButton = document.getElementById("test-button");
    const fileNameSpan = document.getElementById("fileName");
    const displayImage = document.getElementById("display-image");
    const resultBox = document.getElementById("result-box");

    let uploadedFileName = "";

    uploadButton.addEventListener("click", function () {
        const fileInput = document.createElement("input");
        fileInput.type = "file";
        fileInput.accept = "image/png, image/jpeg, image/jpg";
        
        fileInput.addEventListener("change", function () {
            const file = fileInput.files[0];
            if (file) {
                fileNameSpan.textContent = file.name;

                const formData = new FormData();
                formData.append("file", file);

                fetch("/upload", {
                    method: "POST",
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        uploadedFileName = data.filename;
                        fileNameSpan.textContent = `Uploaded: ${data.filename}`;
                        displayImage.src = `/static/uploads/${data.filename}`;
                        testButton.disabled = false;
                        resultBox.style.display = 'none';
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                });
            }
        });

        fileInput.click();
    });

    testButton.addEventListener("click", function () {
        if (!uploadedFileName) {
            alert("Please upload a file first.");
            return;
        }

        const formData = new FormData();
        formData.append("filename", uploadedFileName);

        fetch("/test", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                resultBox.textContent = `Predicted Label: ${data.predicted_label}`;
                resultBox.style.display = 'block'; // Show result box
                testButton.disabled = true;
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });

    // Disable test button initially
    testButton.disabled = true;
});
