import HomePage from "./pages/HomePage.vue";
import EventPage from "./pages/EventPage.vue";
import EventsPage from "./pages/EventsPage.vue";
import ComparePage from "./pages/ComparePage.vue";
// import NotFound from "./pages/NotFoundPage";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage
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
  // {
  //   path: "*",
  //   name: "notFound",
  //   component: NotFound
  // }
];

export default routes;