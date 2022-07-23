/*
Fade in function for html elements
*/

function Fader(elementSelector){
    /* elementSelector must be a CSS identifier */

    if(typeof elementSelector !=='string'){
        throw new Error('input must be a string identifier.')
    }

    const fadeElements = document.querySelectorAll(`${elementSelector}`);

    const fadeOptions = {
        root: null,
        rootMargin: "50px 0px 25px 0px",
        threshold: 0.5,
    };

    const FadeObserver = new IntersectionObserver(
    (entries)=>{
        entries.forEach(entry=>{
            if(!entry.isIntersecting){
                entry.target.classList.remove(`appear`)
                return;
            }
            entry.target.classList.add('appear');
        })
    },
    fadeOptions
    )

    fadeElements.forEach(fElement=>{FadeObserver.observe(fElement)})
}

export default Fader()