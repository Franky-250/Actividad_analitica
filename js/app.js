document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll("nav ul li a");
  const content = document.getElementById("content");

  // Verificar la última vista visitada almacenada en LocalStorage
  const lastView = localStorage.getItem("lastView");

  if (lastView) {
    loadView(lastView); 
  } else {
    loadView("portada"); 
  }

  
  links.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const view = link.getAttribute("data-view");
      localStorage.setItem("lastView", view); 
      loadView(view);
    });
  });

  
  function loadView(view) {
    fetch(`view/${view}.html`)
      .then((response) => {
        if (!response.ok) throw new Error("Vista no encontrada");
        return response.text();
      })
      .then((html) => {
        content.innerHTML = html;
      })
      .catch(() => {
        content.innerHTML = "<p>Error al cargar la vista. Por favor, verifica el archivo.</p>";
      });
  }
});
