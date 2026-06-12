# TODO - Fix Login/Logout

- [x] Detectar y corregir vista/ruta de logout inexistente.
- [x] Implementar `logout_view` en `apps/usuarios/views.py` para limpiar `request.session`.
- [x] Agregar ruta `logout/` en `apps/usuarios/urls.py`.
- [x] Actualizar `templates/base.html` para que el botón “Cerrar sesión” apunte a `logout`.
- [ ] Ejecutar servidor y probar: login -> cierre -> vuelve a login sin mantener sesión.


