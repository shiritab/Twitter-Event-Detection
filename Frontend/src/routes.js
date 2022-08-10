import HomePage from "./pages/HomePage.vue";
import EventPage from "./pages/EventPage.vue";
import EventsPage from "./pages/EventsPage.vue";
import ComparePage from "./pages/ComparePage.vue";
import LoginPage from "./pages/LoginPage.vue";
// import NotFound from "./pages/NotFoundPage";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/Event/:id",
    name:"event",
    component: EventPage,
    props: true
  },
  {
    path: "/Event",
    name:"events",
    component: EventsPage 
  },
  {
    path: "/Compare",
    name:"compare",
    component: ComparePage 
  },
  {
    path: "/Login",
    name:"login",
    component: LoginPage 
  },
  {
    path: "/register",
    name: "register",
    component: () => import("./pages/RegisterPage")
  },
  {
    path: "/about",
    name: "about",
    component: () => import("./pages/AboutPage")
  },
  {
    path: "/help",
    name: "help",
    component: () => import("./pages/HelpPage")
  },
  // {
  //   path: "*",
  //   name: "notFound",
  //   component: NotFound
  // }
];



export default routes;