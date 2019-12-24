<template>
    <div class="md:w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar">
        <Label :text="event.types" />
        <div class="flex flex-col h-72 mt-12 pb-12">
            <div class="font-extrabold text-xl leading-180">
                {{ event.title.toUpperCase() }}
            </div>
            <div class="mt-8 text-base font-semibold leading-170">
                {{ event.timing }}
            </div>
            <div class="mt-16 text-base leading-normal">
                {{ event.description }}
            </div>
        </div>
        <div
            class="flex flex-col mt-12 pb-10"
            v-for="(eventUpdates, index) in eventUpdates"
            v-bind:key="eventUpdates"
        >
            <div class="font-semibold text-base leading-170">
                {{ index + 1 }} Updates
            </div>
            <UpdateCard
                :title="eventUpdates.title"
                :description="eventUpdate.description"
            />
        </div>
        <div class="mt-10 font-extrabold text-base text-red pb-8 leading-170">
            Know more
        </div>
    </div>
</template>

<script>
import Label from "@/components/Label.vue";
import UpdateCard from "@/components/news/UpdateCard.vue";
export default {
    name: "largefeed",
    components: {
        Label,
        UpdateCard
    },
    props: {
        event: Object,
        eventUpdates: Array
    }
};
</script>
