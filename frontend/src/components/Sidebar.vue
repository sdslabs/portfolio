<template>
    <ul
        class="hidden fixed z-10 h-screen bg-white flex-col pt-navbar justify-center list-reset pl-16 sm:flex sm:pl-36 sm:w-88 "
    >
        <SideLink
            v-for="(project, permalink, index) in projects"
            v-bind:key="index"
            v-bind:permalink="permalink"
            v-bind:title="project.title"
            v-bind:isActive="isActive == project.permalink"
        />
    </ul>
</template>

<script>
import SideLink from "@/components/sidebar/SideLink.vue";

function handleIntersect(entries, observer) {
    for (let i = 0; i < entries.length; i++) {
        let entry = entries[i];
        if (entry.isIntersecting) this.isActive = entry.target.id;
    }
}

export default {
    name: "sidebar",
    props: {
        projects: {
            type: Object,
            required: true
        },
        isVisible: {
            type: Boolean,
            default: false
        }
    },
    data: function initData() {
        return {
            observer: undefined,
            isObserverSet: false,
            isActive: ""
        };
    },
    components: {
        SideLink
    },
    methods: {
        handleIntersect: handleIntersect
    },
    updated() {
        if (!this.isObserverSet && Object.keys(this.projects).length > 0) {
            let keys = Object.keys(this.projects);
            let options = {
                root: null,
                rootMargin: "0px",
                threshold: 0.51
            };
            let observer = new IntersectionObserver(
                this.handleIntersect,
                options
            );
            for (let i = 0; i < keys.length; i++) {
                let el = document.querySelector("#" + keys[i]);
                observer.observe(el);
            }
            this.isObserverSet = true;
            this.observer = observer;
        }
    },
    destroyed() {
        this.observer.disconnect();
    }
};
</script>
