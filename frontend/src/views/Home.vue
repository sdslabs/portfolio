<template>
    <div id="home" @click="close">
        <Sidebar v-bind:projects="projects" v-bind:isVisible="true" />
        <div
            id="home"
            class="z-20 relative pt-38 sm:pt-0 bg-white fullpage section"
        >
            <Landing />
        </div>
        <div
            class="px-16 sm:px-88 pb-28 sm:pb-0 flex flex-col justify-center items-center"
            id="projects"
        >
            <Project
                :data-anchor="index"
                class="fullpage section"
                v-for="(project, permalink, index) in projects"
                v-bind:key="index"
                v-bind:title="project.title"
                v-bind:desc="project.description"
                v-bind:url="project.url"
                v-bind:image_url="project.image"
                v-bind:permalink="project.permalink"
                v-bind:color="project.color"
            />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Router from "@/router.js";
import Sidebar from "@/components/Sidebar.vue";
import Landing from "@/components/Landing.vue";
import Project from "@/components/Project.vue";
import { CONFIG } from "@/utils/constants.js";
import { CLOSE_USER } from "@/mutation-types";

let scrollOptions = { behavior: "smooth", block: "start" };

// eslint-disable-next-line
function handleIntersect(entries, observer) {
    let projectsElement = document.querySelector("#projects");
    if (projectsElement == null) return;
    for (let i = 0; i < entries.length; i++) {
        let entry = entries[i];
        if (entry.intersectionRatio > 0.05 && this.$route.name != "projects") {
            this.auto = true;
            Router.push({ name: "projects" });
        } else if (
            entry.intersectionRatio < 0.05 &&
            this.$route.name != "home"
        ) {
            this.auto = true;
            Router.push({ name: "home" });
        }
    }
}

function createObserver() {
    let observer;
    let options = {
        root: null,
        rootMargin: "0px",
        threshold: [0, 1.5 / 30]
    };
    observer = new IntersectionObserver(this.handleIntersect, options);
    return observer;
}

export default {
    name: "home",
    components: {
        Sidebar,
        Landing,
        Project
    },
    data: function initData() {
        return {
            projects: {},
            auto: false,
            isObserverSet: 0,
            observer: undefined
        };
    },
    watch: {
        $route: function(to, from) {
            let projectsElement = document.querySelector("#projects");
            let homeElement = document.querySelector("#home");

            if (!this.auto) {
                if (to.name == "projects" && from.name == "home") {
                    projectsElement.scrollIntoView(scrollOptions);
                } else if (to.name == "home" && from.name == "projects") {
                    homeElement.scrollIntoView(scrollOptions);
                }
            } else {
                this.auto = false;
            }
        }
    },
    methods: {
        close() {
            this.$store.commit(CLOSE_USER);
        },
        createObserver: createObserver,
        handleIntersect: handleIntersect
    },
    mounted() {
        window.scrollTo(0, 0);
        axios
            .get(`${CONFIG.baseURL}/api/projects/?format=json`)
            .then(response => {
                let projects = {};
                for (let i = 0; i < response.data.length; i++) {
                    projects[response.data[i]["permalink"]] = response.data[i];
                }
                this.projects = Object.assign({}, this.projects, projects);
            });
    },
    updated() {
        if (!this.isObserverSet && Object.keys(this.projects).length > 0) {
            let currentRoute = this.$route;
            let projectsElement = document.querySelector("#projects");
            if (currentRoute.name == "projects") {
                projectsElement.scrollIntoView(scrollOptions);
            }
            let observer = this.createObserver();
            setTimeout(function() {
                observer.observe(projectsElement);
                this.observer = observer;
                this.isObserverSet = true;
            }, 1);
        }
    },
    destroyed() {
        this.observer.disconnect();
    }
};
</script>
