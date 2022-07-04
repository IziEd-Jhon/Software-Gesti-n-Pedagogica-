import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Dashboard from "../views/Dashboard.vue";
import AlumnoInicio from "../views/Alumnos/Home/Inicio.vue";
import ProfesorInicio from "../views/Profesores/Home/Inicio.vue";

// Component Pages

var appname = "- Izied LMS  ";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: { title: "Page One " + appname },
  },
  {
    path: "/login",
    name: "login",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/LoginView.vue"),
      meta: { title: "Login " + appname },
  },
  
  {
    path: "/app/homepage",
    name: "Dashboard",
    component: Dashboard,
    meta: { title: "Dashboard " + appname },
  },

  {
    path: "/app/alumno/home",
    name: "InicioAlumno",
    component: AlumnoInicio,
    meta: { title: "Inicio Alumno " + appname },
  },
  {
    path: "/app/profesor/home",
    name: "InicioProfesor",
    component: ProfesorInicio,
    meta: { title: "Inicio Profesor " + appname },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
