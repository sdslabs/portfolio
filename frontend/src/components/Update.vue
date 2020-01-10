<template>
    <div class="flex flex-col sm:flex-row mt-16 mb-32">
        <div class="sm:w-feed flex flex-col mt-16">
            <div class="font-extrabold text-xl leading-180">
                {{ title.toUpperCase() }}
            </div>
            <div
                :class="timing ? 'font-semibold text-base mt-14' : 'hidden'"
                class="leading-normal text-grey"
            >
                {{ timing }}
            </div>
            <div
                :class="description ? 'text-base mt-20' : 'hidden'"
                class="leading-normal text-grey"
            >
                {{ description }}
            </div>
            <div class="text-base mt-14 text-grey leading-normal">
                {{ contactInfo }}
            </div>
            <div class="text-base mt-14 text-grey leading-normal">
                {{ footNote }}
            </div>
            <div class="text-base mt-14 text-grey leading-normal">
                {{ greetings }}
            </div>
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
        contactInfo: String,
        footNote: String,
        greetings: String,
        url: String,
        image: String
    }
};
</script>
