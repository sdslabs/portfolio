<template>
    <div class="flex flex-col sm:flex-row mt-16 mb-32">
        <div class="sm:w-feed flex flex-col sm:ml-60 mt-16">
            <div class="font-extrabold text-xl leading-180">{{ title.toUpperCase() }}</div>
            <div
                :class="
                    timing ? 'font-semibold text-base mt-14' : 'text-base mt-20'
                "
                class="leading-normal"
            >
                {{ timing ? timing : description }}
            </div>
            <div class="text-base mt-14 leading-normal">{{ description1 }}</div>
            <div class="text-base mt-14 leading-normal">{{ description2 }}</div>
            <div class="text-base mt-14 leading-normal">{{ description3 }}</div>
        </div>
        <div class="sm:w-image">
            <img
                class="mt-12 sm:mt-0 sm:ml-44 sm:w-image shadow-image"
                :src="image"
            />
        </div>
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
        url: String,
        image: String
    }
};
</script>
