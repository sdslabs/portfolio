<template>
    <div class="home-wrapper">
        <Landing />
        <div class="project-wrapper px-16 sm:px-88 flex flex-col justify-center items-center">
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

import Landing from "@/components/Landing.vue";
import Project from "@/components/Project.vue";

export default {
    name: "home",
    components: {
        Landing,
        Project
    },
    data: function initData() {
        return {
            projects: {}
        }
    },
    mounted() {
        axios
            .get('http://10.42.0.1:8000/api/projects/?format=json')
            .then(response => {
                let projects = {}
                for(let i = 0; i < response.data.length; i++) {
                    projects[response.data[i]["permalink"]] = response.data[i]
                }
                this.projects = Object.assign({}, this.projects, projects);
            })
    }
};
</script>
