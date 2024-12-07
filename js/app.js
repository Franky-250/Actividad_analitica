document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll("nav ul li a");
  const content = document.getElementById("content");

  // Cargar contenido inicial (Portada por defecto)
  loadView("portada");

  // Añadir evento de clic a los enlaces del menú
  links.forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const view = link.getAttribute("data-view");
      loadView(view);
    });
  });

  // Función para cargar vistas dinámicamente
  function loadView(view) {
    fetch(`view/${view}.html`)
      .then(response => {
        if (!response.ok) throw new Error("Vista no encontrada");
        return response.text();
      })
      .then(html => {
        content.innerHTML = html;
      })
      .catch(() => {
        content.innerHTML = "<p>Error al cargar la vista. Por favor, verifica el archivo.</p>";
      });
  }
});
