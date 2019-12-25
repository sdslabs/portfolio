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
            path: "/news",
            name: "news",
            component: () =>
                import(/* webpackChunkName: "about" */ "./views/News.vue"),
            meta: {
                title: "SDSLabs | News"
            }
        },
        {
            path: "/news/event/:title",
            name: "event",
            props: true,
            component: () =>
                import(/* webpackChunkName: "about" */ "./views/Event.vue"),
            meta: {
                title: "SDSLabs | News"
            }
        }
    ]
});

router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    next();
});

export default router;
