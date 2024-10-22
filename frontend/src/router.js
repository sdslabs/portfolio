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
                title: "SDSLabs",
                hideFooter: true
            }
        },
        {
            path: "/projects",
            name: "projects",
            component: Home,
            props: true,
            meta: {
                title: "SDSLabs | Projects",
                hideFooter: true
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
            path: "/news/:title",
            name: "event",
            props: true,
            component: () =>
                import(/* webpackChunkName: "about" */ "./views/Event.vue"),
            meta: {
                title: "SDSLabs | News"
            }
        },
        {
            path: "/contact",
            name: "contact",
            component: () => import("./views/Contact.vue"),
            meta: {
                title: "SDSLabs | Contact",
                hideFooter: true
            }
        },
        {
            path: "/recruitments-2y",
            name: "recruitments-2y"
        },
        {
            path: "*",
            name: "error404",
            component: () => import("./views/Error404.vue"),
            meta: {
                title: "SDSLabs | Error",
                hideFooter: true
            }
        }
    ]
});

router.beforeEach((to, from, next) => {
    if (to.path === "/recruitments-2y") {
        window.location.href =
            "https://magical-meteoroid-2c8.notion.site/SDSLabs-Sophomore-Recruitment-2023-8ba4def1f5734f768d6f6b33ef8ae803?pvs=4";
    } else {
        document.title = to.meta.title;
        next();
    }
});

export default router;
