document.addEventListener("DOMContentLoaded", () => { 
    document.querySelectorAll("td.precioadmin").forEach(el => {
        let texto = el.textContent.trim();
        let num = parseFloat(texto.replace(",", "."));

        const opciones = Number.isInteger(num)
            ? {}
            : { minimumFractionDigits: 2 };

        el.textContent = num.toLocaleString("en-US", opciones);
    });

    const btnIrArriba = document.getElementById("btn-ir-arriba");
    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) {
            btnIrArriba.classList.add("mostrar");
        } else {
            btnIrArriba.classList.remove("mostrar");
        }
    });
    btnIrArriba.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    const botones = document.querySelectorAll('.btnsnd');
    const hoverSound = document.getElementById('hoversound');
    const clickSound = document.getElementById('clicksound');

    botones.forEach(boton => {
        // Sonido al pasar el mouse
        boton.addEventListener('mouseenter', () => {
            hoverSound.currentTime = 0;
            hoverSound.play().catch(console.warn);
        });

        // Sonido al hacer clic
        boton.addEventListener('click', () => {
            clickSound.currentTime = 0;
            clickSound.play().catch(console.warn);
        });
    });
    document.querySelectorAll("td.precioadmin").forEach(el => {
        let texto = el.textContent.trim();
        let num = parseFloat(texto.replace(",", "."));

        const opciones = Number.isInteger(num)
            ? {}
            : { minimumFractionDigits: 2 };

        el.textContent = num.toLocaleString("en-US", opciones);
    });

    /* ==== STOCK EN ROJO + NEGRITA + ⚠ ==== */
    document.querySelectorAll("td.stock").forEach(el => {
        let texto = el.textContent.trim();
        let stock = parseInt(texto, 10);

        if (!Number.isNaN(stock) && stock < 5) {
            el.style.color = "red";
            el.style.fontWeight = "bold";
            el.textContent = `${stock} ⚠`;
        }
    });
    const inputFile = document.getElementById("id_Imagen");
    const preview = document.getElementById("imgPreview");

    if (inputFile) {
        inputFile.addEventListener("change", function() {
            const file = inputFile.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.style.display = "block";
                };
                reader.readAsDataURL(file);
            } else {
                preview.src = "";
                preview.style.display = "block";
            }
        });
    }
});