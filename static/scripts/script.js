document.getElementById("fileInput").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const previewImg = document.getElementById("previewImg");
            previewImg.src = e.target.result;
            previewImg.style.display = "block";
        }
        reader.readAsDataURL(file);
    }
});
