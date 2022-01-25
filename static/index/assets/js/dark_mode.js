// Dark Mode
let darkMode = localStorage.getItem('darkMode'); 
let edcImg = document.querySelector("#edc-img");
let successImg = document.querySelector("#success-img");
let logoImg=document.querySelector("#logoimg")


const darkModeToggle = document.querySelector('#darkToggle');

const enableDarkMode = () => {
  document.body.classList.add('darkmode');
  darkModeToggle.classList.remove('bi-moon-fill');
  darkModeToggle.classList.add('bi-sun-fill');
  logoImg.setAttribute("src", logoImageDark);
  localStorage.setItem('darkMode', 'enabled');
}

const disableDarkMode = () => {
  document.body.classList.remove('darkmode');
  darkModeToggle.classList.remove('bi-sun-fill');
  darkModeToggle.classList.add('bi-moon-fill');
  logoImg.setAttribute("src", logoImage);
  localStorage.setItem('darkMode', null);
}
 
if (darkMode === 'enabled') {
  enableDarkMode();
}
else{
  disableDarkMode();
}

darkModeToggle.addEventListener('click', () => {
  darkMode = localStorage.getItem('darkMode'); 
  
  if (darkMode !== 'enabled') {
    enableDarkMode();
  } else {  
    disableDarkMode(); 
  }

});
