class CButton extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        const button = document.createElement('button');
        const buttonText = this.textContent.trim()
       
        button.textContent = buttonText;
        button.addEventListener('click', () => {
            alert("Button Clicked!");
        });
        this.shadowRoot.appendChild(button);
    }
}

export default CButton;
