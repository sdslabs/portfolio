<template>
    <div id="home" class="home">
        <Sidebar v-bind:projects="projects" v-bind:isVisible="true" />
        <section class="fullpage">
            <div id="home" class="z-20 relative bg-white">
                <Landing />
            </div>
        </section>
        <section class="fullpage">
            <div
                class="px-16 sm:px-88 pb-28 sm:pb-0 flex flex-col justify-center items-center"
                id="projects"
            >
                <Project
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
        </section>
    </div>
</template>

<script>
import axios from "axios";
import Router from "@/router.js";
import Sidebar from "@/components/Sidebar.vue";
import Landing from "@/components/Landing.vue";
import Project from "@/components/Project.vue";
import { CONFIG } from "@/utils/constants.js";

let scrollOptions = { behavior: "smooth", block: "start" };

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
            observer: undefined,
            inMove: false,
            activeSection: 0,
            offsets: [],
            touchStartY: 0
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
        createObserver: createObserver,
        handleIntersect: handleIntersect,
        calculateSectionOffsets() {
            let sections = document.getElementsByTagName("section");
            let length = sections.length;
            for (let i = 0; i < length; i++) {
                let sectionOffset = sections[i].offsetTop;
                this.offsets.push(sectionOffset);
            }
        },
        scrollToSection(id, force = false) {
            if (this.inMove && !force) return false;
            this.activeSection = id;
            this.inMove = true;
            document.getElementsByTagName("section")[id].scrollIntoView({
                behavior: "smooth"
            });
            setTimeout(() => {
                this.inMove = false;
            }, 400);
        },
        handleMouseWheel: function(e) {
            if (e.wheelDelta < 30 && !this.inMove) {
                this.moveUp();
            } else if (e.wheelDelta > 30 && !this.inMove) {
                this.moveDown();
            }
            e.preventDefault();
            return false;
        },
        moveDown() {
            this.inMove = true;
            this.activeSection--;
            if (this.activeSection < 0)
                this.activeSection = this.offsets.length - 1;
            this.scrollToSection(this.activeSection, true);
        },
        moveUp() {
            this.inMove = true;
            this.activeSection++;
            if (this.activeSection > this.offsets.length - 1)
                this.activeSection = 0;
            this.scrollToSection(this.activeSection, true);
        },
        touchStart(e) {
            e.preventDefault();
            this.touchStartY = e.touches[0].clientY;
        },
        touchMove(e) {
            if (this.inMove) return false;
            e.preventDefault();
            const currentY = e.touches[0].clientY;
            if (this.touchStartY < currentY) {
                this.moveDown();
            } else {
                this.moveUp();
            }
            this.touchStartY = 0;
            return false;
        }
    },
    mounted() {
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
    created() {
        // this.calculateSectionOffsets();
        // window.addEventListener("mousewheel", this.handleMouseWheel, {
        //     passive: false
        // });
        // window.addEventListener("touchstart", this.touchStart, {
        //     passive: false
        // });
        // window.addEventListener("touchmove", this.touchMove, {
        //     passive: false
        // });
    },
    destroyed() {
        this.observer.disconnect();
        //     window.removeEventListener("DOMMouseScroll", this.handleMouseWheelDOM);
        //     window.removeEventListener("touchstart", this.touchStart);
        //     window.removeEventListener("touchmove", this.touchMove);
    }
};
</script>
