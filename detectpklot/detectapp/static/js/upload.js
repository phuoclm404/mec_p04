const handleChange = () => {
  const fileUploader = document.querySelector("#input-file");
  const getFile = fileUploader.files;
  if (getFile.length !== 0) {
    const uploadedFile = getFile[0];
    readFile(uploadedFile);
  }
};

const readFile = (uploadedFile) => {
  if (uploadedFile) {
    const reader = new FileReader();
    reader.onload = () => {
      const parent = document.querySelector(".preview-box");
      parent.innerHTML = `<img class="preview-content" src=${reader.result} />`;
    };

    reader.readAsDataURL(uploadedFile);
  }
};
