<template>
    <div class="flex flex-row mt-16 mb-32">
        <div class="w-feed flex flex-col ml-68 mt-16">
            <div class="font-extrabold text-xl">{{title}}</div>
            <div :class="timing ? 'font-semibold text-base mt-14' : 'text-base mt-20'">{{timing ? timing : description}}</div>
            <div class="text-base mt-14">{{description1}}</div>
            <div class="text-base mt-14">{{description2}}</div>
            <div class="text-base mt-14">{{description3}}</div>
        </div>
        <div class="ml-44 shadow-image"><img class="w-image" :src="url"/></div>
    </div>
</template>

<script>
export default {
    name: "update",
    props: {
        title: String,
        timing: String,
        description: String,
        description1: String,
        description2: String,
        description3: String,
        url: String
    }
}
</script>
