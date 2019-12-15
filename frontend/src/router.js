import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

const router = new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            name: "home",
            component: Home,
            props: true,
            meta: {
                title: "SDSLabs"
            }
        },
        {
            path: "/projects",
            name: "projects",
            component: Home,
            props: true,
            meta: {
                title: "SDSLabs | Projects"
            }
        },
        {
            path: "/about",
            name: "about",
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () =>
                import(/* webpackChunkName: "about" */ "./views/About.vue"),
            meta: {
                title: "SDSLabs | About Us"
            }
        },
        {
            path: "*",
            name: "error404",
            component: () => import("./views/Error404.vue"),
            meta: {
                title: "SDSLabs | Error"
            }
        }
    ]
});

router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    next();
});

export default router;
