setTimeout(fade_out, 6000);
function fade_out() {
    $(".alert-message").fadeOut('slow');
}

const boxes = document.querySelectorAll('.service-box')

window.addEventListener('scroll', checkBoxes)

checkBoxes()

function checkBoxes() {
    const triggerBottom = window.innerHeight / 4 * 3

    boxes.forEach(box => {
        const boxTop = box.getBoundingClientRect().top

        if(boxTop < triggerBottom) {
            box.classList.add('show')
        } else{
            box.classList.remove('show')
        }
    })
}