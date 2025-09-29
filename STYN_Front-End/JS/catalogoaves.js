// Datos de las aves de Nicaragua
const avesData = {
    guardabarranco: {
        title: "Guardabarranco",
        description: "Ave nacional de Nicaragua",
        tag: "Eumomota superciliosa",
        image: "../Image/guardabarranco.jpg",
        fullInfo: "El Guardabarranco es el ave nacional de Nicaragua desde 1971. Se caracteriza por su plumaje verde, azul y naranja, y su larga cola con plumas en forma de raquetas. Habita en zonas boscosas y se alimenta de insectos, lagartijas y frutas."
    },
    zopilote: {
        title: "Zopilote",
        description: "Ave carroñera común",
        tag: "Coragyps atratus", 
        image: "../Image/zopilote.jpg",
        fullInfo: "El Zopilote Negro es un ave carroñera que cumple un papel crucial en el ecosistema al limpiar los restos de animales muertos. Tiene una envergadura de hasta 1.5 metros y excelente sentido del olfato para localizar carroña."
    },
    colibri: {
        title: "Colibrí Esmeralda",
        description: "Pequeño y colorido",
        tag: "Chlorostilbon canivetii",
        image: "../Image/colibri.jpg",
        fullInfo: "El Colibrí Esmeralda es una de las aves más pequeñas de Nicaragua. Puede batir sus alas hasta 80 veces por segundo y es capaz de volar en todas direcciones, incluso hacia atrás. Se alimenta del néctar de flores y pequeños insectos."
    },
    chocoyo: {
        title: "Chocoyo",
        description: "Loro centroamericano",
        tag: "Amazona albifrons",
        image: "../Image/chocoyo.jpg",
        fullInfo: "El Chocoyo o Loro Frentiblanco es un loro mediano muy social que vive en grandes bandadas. Anida en cavidades de árboles y acantilados. Es conocido por su capacidad para imitar sonidos y su longevidad (puede vivir hasta 50 años)."
    },
    zanate: {
        title: "Zanate",
        description: "Ave de canto melodioso",
        tag: "Quiscalus nicaraguensis",
        image: "../Image/zanate.jpg",
        fullInfo: "El Zanate Nicaragüense es endémico de Nicaragua. El macho es completamente negro con ojos amarillos, mientras que la hembra es café. Es omnívoro y se adapta fácilmente a enturbanos. Su canto es complejo y melodioso."
    },
    pijuy: {
        title: "Pijuy",
        description: "Cuco terrestre",
        tag: "Crotophaga sulcirostris",
        image: "../Image/pijuy.jpg",
        fullInfo: "El Pijuy o Garrapatero es un cuco terrestre que se alimenta de insectos, especialmente garrapatas que extrae del pelaje de animales. Vive en grupos familiares y todos los miembros cooperan en el cuidado de los polluelos."
    },
    urraca: {
        title: "Urraca",
        description: "Ave inteligente y social",
        tag: "Calocitta formosa",
        image: "../Image/urraca.jpg",
        fullInfo: "La Urraca Hermosa Cariblanca es conocida por su inteligencia y comportamiento social. Tiene un plumaje llamativo azul, blanco y negro, y una cola muy larga. Es omnívora y se comunica con una variedad de vocalizaciones complejas."
    },
    gavilan: {
        title: "Gavilán Colirrojo",
        description: "Ave rapaz común",
        tag: "Buteo jamaicensis",
        image: "../Image/gavilan.jpg",
        fullInfo: "El Gavilán Colirrojo es una rapaz común en Nicaragua. Se alimenta principalmente de roedores, reptiles y pequeños pájaros. Tiene una envergadura de hasta 1.3 metros y excelente vista para localizar presas desde grandes alturas."
    }
};

// Elementos del modal
const modal = document.getElementById('modalAve');
const modalImg = document.getElementById('modal-img');
const modalTitle = document.getElementById('modal-title');
const modalDescription = document.getElementById('modal-description');
const modalTag = document.getElementById('modal-tag');
const modalFullInfo = document.getElementById('modal-full-info');
const closeModal = document.querySelector('.close-modal');

// Abrir modal
document.querySelectorAll('.btn-modal').forEach(button => {
    button.addEventListener('click', function() {
        const birdType = this.getAttribute('data-bird');
        const birdData = avesData[birdType];
        
        if (birdData) {
            modalImg.src = birdData.image;
            modalImg.alt = birdData.title;
            modalTitle.textContent = birdData.title;
            modalDescription.textContent = birdData.description;
            modalTag.textContent = birdData.tag;
            modalFullInfo.textContent = birdData.fullInfo;
            
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        }
    });
});

// Cerrar modal
closeModal.addEventListener('click', function() {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
});

// Cerrar modal al hacer clic fuera
window.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});

// Cerrar con tecla ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});