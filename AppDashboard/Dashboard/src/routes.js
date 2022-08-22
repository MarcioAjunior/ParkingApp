import Index from "views/Index.js";
import Maps from "views/examples/Maps.js";
import ViewVagasId from "views/examples/VagasId.js";

var routes = [
  {
    path: "/index",
    name: "Dashboard",
    icon: "ni ni-tv-2 text-primary",
    component: Index,
    layout: "/admin",
    show : true
  },
  {
    path: "/vagas",
    name: "Vagas",
    icon: "ni ni-pin-3 text-orange",
    component: Maps,
    layout: "/admin",
    exact : true,
    show : true
  },
  {
    path: "/vagas/:id",
    name: "Alou",
    icon: "ni ni-pin-3 text-orange",
    component: ViewVagasId,
    layout: "/admin",
    exact : true,
    show : false
  },
  
];
export default routes;
