<template>
    <li
        class="my-6 font-medium text-xs uppercase cursor-pointer"
        v-on:click="linkClickHandler"
        :class="isActive ? 'text-xl font-bold' : ''"
    >
        {{ title }}
    </li>
</template>

<script>
function linkClickHandler() {
    let element = document.querySelector("#" + this.permalink);
    let scrollOptions = { behavior: "smooth", block: "start" };
    element.scrollIntoView(scrollOptions);
}

export default {
    name: "sidelink",
    methods: {
        linkClickHandler: linkClickHandler
    },
    props: {
        permalink: {
            type: String,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        isActive: {
            type: Boolean,
            required: true
        }
    }
};
</script>
