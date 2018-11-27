<template>
    <div>
        <div id="home">
            <Landing />
        </div>
        <div class="px-16 sm:px-88 flex flex-col justify-center items-center" id="projects">
            <Project
                v-for="(project, permalink, index) in projects"
                v-bind:key="index"
                v-bind:title="project.title"
                v-bind:desc="project.description"
                v-bind:url="project.url"
                v-bind:image_url="project.image"
            />
        </div>
    </div>
</template>

<script>

import axios from "axios";

import Router from '@/router.js';
import Landing from "@/components/Landing.vue";
import Project from "@/components/Project.vue";

let scrollOptions = {behavior: "smooth", block: "start"};

function handleIntersect(entries, observer) {
    let projectsElement = document.querySelector("#projects");
    if (projectsElement == null)
        return;
    console.log("Handling intersect");
    for(let i = 0; i < entries.length; i++) {
        let entry = entries[i];
        if (entry.intersectionRatio > this.prevRatio) {
            Router.push({ name: 'projects' })
        } else if (entry.intersectionRatio < this.prevRatio) {
            Router.push({ name: 'home' })
        }
        this.prevRatio = entry.intersectionRatio;
    }
}

function createObserver(el) {
    let observer;
    let options = {
        root: null,
        rootMargin: "0px",
        threshold: [0, 1.5/30]
    };
    observer = new IntersectionObserver(this.handleIntersect, options);
    observer.observe(el);
    this.observer = observer;
}

export default {
    name: "home",
    components: {
        Landing,
        Project
    },
    data: function initData() {
        return {
            projects: {},
            prevRatio: 0,
            isObserverSet: 0,
            observer: undefined
        }
    },
    watch: {
        '$route': function(to, from) {
            let projectsElement = document.querySelector("#projects");
            let homeElement = document.querySelector("#home");

            if (this.prevRatio < 0.05) {
                if(to.name == "projects" && from.name == "home") {
                    projectsElement.scrollIntoView(scrollOptions);
                    this.prevRatio = 0.050000001;
                }
            } else {
                if(to.name == "home" && from.name == "projects") {
                    homeElement.scrollIntoView(scrollOptions);
                    this.prevRatio = 0.049999999;
                }
            }
        }
    },
    methods: {
        createObserver: createObserver,
        handleIntersect: handleIntersect
    },
    mounted() {
        axios
            .get('http://0.0.0.0:8000/api/projects/?format=json')
            .then(response => {
                let projects = {}
                for(let i = 0; i < response.data.length; i++) {
                    projects[response.data[i]["permalink"]] = response.data[i]
                }
                this.projects = Object.assign({}, this.projects, projects);
            })
    },
    updated() {
        if (!this.isObserverSet && Object.keys(this.projects).length > 0) {
            let currentRoute = this.$route;
            let projectsElement = document.querySelector("#projects");
            this.createObserver(projectsElement);
            if (currentRoute.name == "projects") {
                console.log("Current route is projects");
                projectsElement.scrollIntoView(scrollOptions);
                this.prevRatio = 0.050000001;
            }
            this.isObserverSet = true;
        }
    }
};
</script>
