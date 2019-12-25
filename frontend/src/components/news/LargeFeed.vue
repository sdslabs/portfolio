<template>
    <div class="md:w-feed h-auto shadow-feed pl-10 pt-10 pr-navbar">
        <Label :text="event.types" />
        <div class="flex flex-col h-auto mt-12 pb-12">
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
        <div v-if="eventUpdates.length != 0">
            <div class="font-semibold text-base pt-14 leading-170">
                {{ eventUpdates.length }} Updates
            </div>
            <div
                class="flex flex-col pb-10"
                v-for="eventUpdates in eventUpdates"
                v-bind:key="eventUpdates"
            >
                <UpdateCard
                    :title="eventUpdates.title"
                    :description="eventUpdates.description"
                />
            </div>
        </div>
        <div class="mt-10 font-extrabold text-base pb-8 leading-170">
            <router-link
                :to="'/news/'+event.title"
                class="no-underline inline-block text-red"
            >
                Know More
            </router-link>
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
        UpdateCard,
    },
    props: {
        event: Object,
        eventUpdates: Array
    }
};
</script>
