const components = document.querySelector('.component');
const ul = document.querySelector('.ul_1')
const main = document.querySelector('.main_header')

components.onmouseover= function(){
    ul.style.display = 'block';
}

components.onmouseout=function(){
    ul.style.display = 'none';
}