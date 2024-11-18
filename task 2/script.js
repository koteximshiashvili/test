document.querySelector('button').addEventListener('click', function(){
    const tax = document.querySelector('.tax').value;
    const tip = document.querySelector('.tip').value;
    const sum = document.querySelector('.sum');
    sum.textContent = "tip: " + tax % tip + "$";
})