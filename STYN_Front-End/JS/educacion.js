// Efectos de scroll suave para navegación
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Animación al hacer scroll
// Reemplaza el observer con esta versión mejorada
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -10% 0px'
});

// Aplica animación a más elementos
document.querySelectorAll('.culture-card, .culture-item, .food-item, .culture-hero').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.8s ease';
    observer.observe(el);
});
// ===== MODALES DE CULTURA =====

// Datos para los modales de cultura
const culturaData = {
    // TRADICIONES
"purisima": {
    title: "La Purísima",
    description: "Celebración religiosa en honor a la Virgen María",
    fullInfo: "La Purísima es la festividad religiosa más importante de Nicaragua, celebrada del 28 de noviembre al 8 de diciembre. Durante estos días, las familias construyen altares decorados con flores, luces y imágenes de la Virgen María.\n\nLos fieles visitan los altares cantando alabanzas y reciben dulces tradicionales como gofio, cajetas y leche burra. Esta tradición une a comunidades enteras en una celebración de fe y cultura.",
    curiosities: "• Es la celebración mariana más grande del mundo\n• Se cantan más de 20 alabanzas diferentes\n• En Granada, la Purísima dura todo el mes de diciembre\n• Los altares compiten en creatividad y belleza"
},
    "gueguense": {
        title: "El Güegüense",
        description: "Obra teatral declarada Patrimonio Cultural Inmaterial de la Humanidad",
        fullInfo: "El Güegüense es una obra teatral satírica que combina elementos indígenas y españoles, representada desde el siglo XVI. Los personajes usan máscaras de madera y visten trajes coloridos. La obra critica el colonialismo español de manera humorística a través de diálogos en español y náhuatl.",
        curiosities: "• Declarado Patrimonio de la Humanidad por la UNESCO en 2005\n• También se le conoce como 'Macho Ratón'\n• Las máscaras son hechas a mano por artesanos de Masaya"
    },
    "fiestas": {
        title: "Fiestas Patronales",
        description: "Celebraciones en honor a los santos patronos de cada ciudad",
        fullInfo: "Cada ciudad y pueblo de Nicaragua celebra su santo patrón con fiestas que incluyen procesiones religiosas, desfiles hípicos, ferias gastronómicas y eventos culturales. Las más famosas son las de Santo Domingo de Guzmán en Managua, San Jerónimo en Masaya y La Asunción en Granada.",
        curiosities: "• Managua celebra a Santo Domingo del 1 al 10 de agosto\n• En Masaya, los bailes folclóricos duran toda la noche\n• Las 'vaquitas' son toros artificiales que corren por las calles"
    },

    // BAILES TÍPICOS
    "baile-gueguense": {
        title: "Baile del Güegüense",
        description: "Danza satírica con máscaras coloridas",
        fullInfo: "Esta danza acompaña la obra teatral del Güegüense y representa el encuentro entre indígenas y españoles. Los bailarines usan máscaras que representan españoles, mestizos e indígenas, realizando movimientos que imitan y satirizan a las autoridades coloniales.",
        curiosities: "• Las máscaras pueden pesar hasta 3 kg\n• El baile incluye 14 personajes principales\n• Se baila principalmente en el departamento de Carazo"
    },
    "palo-mayo": {
        title: "Palo de Mayo",
        description: "Baile afrocaribeño lleno de energía y color",
        fullInfo: "Originario de la Costa Caribe nicaragüense, el Palo de Mayo se baila alrededor de un palo decorado con cintas de colores. Los bailarines trenzan y destrenzan las cintas mientras realizan movimientos sensuales y enérgicos al ritmo de tambores y maracas.",
        curiosities: "• Se celebra todo el mes de mayo en Bluefields\n• Las cintas representan la fertilidad y la naturaleza\n• La música mezcla inglés criollo con español"
    },
    "inditas": {
        title: "Baile de las Inditas",
        description: "Danza que representa las labores cotidianas de las mujeres indígenas",
        fullInfo: "Este baile folclórico representa las actividades diarias de las mujeres indígenas como moler maíz, cargar agua y cuidar a los hijos. Las bailarinas visten trajes tradicionales con faldas largas y blusas bordadas, moviéndose con gracia y elegancia.",
        curiosities: "• Es popular en las fiestas patronales de Masaya\n• Los movimientos imitan el moler maíz en piedra\n• Se baila al son de marimba y guitarra"
    },

    // GASTRONOMÍA
    "gallo-pinto": {
        title: "Gallo Pinto",
        description: "El desayuno nacional por excelencia",
        fullInfo: "Plato hecho de arroz y frijoles rojos revueltos, cocinados con cebolla, ajo y chiltoma. Se sirve tradicionalmente con huevo frito, plátano maduro, queso y tortillas. Es el desayuno más común en los hogares nicaragüenses.",
        curiosities: "• Se llama 'gallo pinto' por su apariencia moteada\n• En la Costa Caribe se hace con aceite de coco\n• Cada familia tiene su receta secreta"
    },
    "nacatamal": {
        title: "Nacatamal",
        description: "Masa de maíz rellena con carne, envuelta en hojas de plátano",
        fullInfo: "El nacatamal es un tamal grande relleno con carne de cerdo o pollo, arroz, papas, tomate, cebolla y hierbas aromáticas. Se envuelve en hojas de plátano y se cocina al vapor por varias horas. Es tradicional los fines de semana y en fechas especiales.",
        curiosities: "• Puede pesar hasta 1 kg\n• Se cocina entre 4 y 6 horas\n• Es tradicional del domingo familiar"
    },
    "vigoron": {
        title: "Vigorón",
        description: "Yuca con chicharrón y ensalada de repollo",
        fullInfo: "Plato originario de Granada que consiste en yuca cocida servida sobre una hoja de chagüite, acompañada de chicharrón crujiente y una ensalada de repollo con tomate. Es muy popular en ferias y puestos callejeros.",
        curiosities: "• Se sirve sobre hojas de chagüite o plátano\n• El nombre viene de 'vigor' por ser energético\n• Es el plato emblemático del Parque Central de Granada"
    },
    "quesillo": {
        title: "Quesillo",
        description: "Tortilla con queso, cebolla y crema",
        fullInfo: "Comida rápida típica de Nagarote y La Paz Centro. Consiste en una tortilla de maíz rellena con queso cuajada fresco, cebolla encurtida en vinagre y crema agria. Se envuelve en plástico o papel y se come caliente.",
        curiosities: "• Nagarote es la 'Capital del Quesillo'\n• El plástico ayuda a derretir el queso\n• Se acompaña con una gaseosa o tiste"
    }
};

// Elementos del modal
const cultureModal = document.getElementById('cultureModal');
const closeCultureModal = document.querySelector('.close-culture-modal');
const modalCultureTitle = document.getElementById('modal-culture-title');
const modalCultureDescription = document.getElementById('modal-culture-description');
const modalCultureFullinfo = document.getElementById('modal-culture-fullinfo');
const modalCultureCuriosities = document.getElementById('modal-culture-curiosities');

// Abrir modal de cultura
document.querySelectorAll('.culture-item, .food-item').forEach(item => {
    item.addEventListener('click', function(e) {
        if (e.target.classList.contains('info-btn')) {
            const modalType = this.getAttribute('data-modal');
            const itemData = culturaData[modalType];
            
            if (itemData) {
                modalCultureTitle.textContent = itemData.title;
                modalCultureDescription.textContent = itemData.description;
                modalCultureFullinfo.textContent = itemData.fullInfo;
                modalCultureCuriosities.textContent = itemData.curiosities;
                
                cultureModal.style.display = 'block';
                document.body.style.overflow = 'hidden';
            }
        }
    });
});

// Cerrar modal
closeCultureModal.addEventListener('click', function() {
    cultureModal.style.display = 'none';
    document.body.style.overflow = 'auto';
});

// Cerrar modal al hacer clic fuera
window.addEventListener('click', function(event) {
    if (event.target === cultureModal) {
        cultureModal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});

// Cerrar con tecla ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        cultureModal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});