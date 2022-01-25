const enableDarkImages = () => {
  edcImg.setAttribute("src", edcImageDark);
  successImg.setAttribute("src", successImageDark);
};

const disableDarkImages = () => {
  edcImg.setAttribute("src", edcImage);
  successImg.setAttribute("src", successImage);
};

if (darkMode === 'enabled') {
    enableDarkImages();
  }
  else{
    disableDarkImages();
}

darkModeToggle.addEventListener('click', () => {
    darkMode = localStorage.getItem('darkMode'); 
    
    if (darkMode == 'enabled') {
      enableDarkImages();
    } else {  
      disableDarkImages(); 
    }
  
  });