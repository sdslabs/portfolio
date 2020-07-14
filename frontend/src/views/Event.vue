<template>
    <div class="event pt-40 sm:pt-60 flex flex-col ml-8 mr-8 sm:ml-0 sm:mr-0">
        <div class="flex flex-col pb-40">
            <div class="flex flex-col sm:flex-row">
                <div class="flex flex-col sm:ml-60 mt-10 sm:mt-0">
                    <router-link to="/news" class="no-underline"
                        ><div class="flex flex-row">
                            <img src="@/assets/images/back-arrow.svg" />
                            <div class="text-lg font-bold text-black ml-4">
                                Back
                            </div>
                        </div></router-link
                    >
                    <div class="mt-24 sm:mt-32">
                        <Label :text="events.event[0].types" />
                    </div>
                    <div
                        class="sm:w-feed mt-20 font-black text-3xl leading-180"
                    >
                        {{ events.event[0].title.toUpperCase() }}
                    </div>
                    <div
                        class="mt-8 text-1.5xl sm:text-base text-grey font-semibold leading-170"
                    >
                        {{ events.event[0].timing }}
                    </div>
                    <div
                        class="sm:w-feed mt-14 text-grey text-1.5xl sm:text-base leading-normal"
                    >
                        {{ events.event[0].shortDescription }}
                    </div>
                    <div class="mt-28">
                        <Button
                            v-if="events.event[0].types !== 'past event'"
                            v-bind:native="true"
                            :url="events.event[0].url"
                            text="Register Now"
                        />
                    </div>
                </div>
                <div class="mt-20 sm:mt-0 sm:ml-44">
                    <img
                        class="sm:w-image shadow-image"
                        :src="events.event[0].image"
                    />
                </div>
            </div>
            <div
                class="sm:ml-60 mt-40 text-1.5xl sm:text-base text-grey sm:w-eventdesc leading-normal"
            >
                {{ events.event[0].fullDescription }}
            </div>
        </div>
        <div
            class="flex flex-col border-border border-t-feed sm:ml-60 sm:mr-36"
            v-if="events.event_update.length != 0"
        >
            <div class="mt-40 font-extrabold text-2xl sm:text-lg leading-170">
                {{ events.event_update.length }} Updates
            </div>
            <div>
                <div
                    v-for="event_update in events.event_update"
                    v-bind:key="event_update"
                >
                    <Update
                        :title="event_update.title"
                        :timing="event_update.timing"
                        :description="event_update.description"
                        :contactInfo="event_update.contactInfo"
                        :footNote="event_update.footNote"
                        :greetings="event_update.greetings"
                        :url="event_update.url"
                        :image="event_update.image"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Label from "@/components/Label.vue";
import Update from "@/components/Update.vue";
import Button from "@/components/Button.vue";
import { CONFIG } from "@/utils/constants.js";
export default {
    name: "event",
    components: {
        Label,
        Button,
        Update
    },
    data() {
        return {
            events: {},
            title: ""
        };
    },
    created() {
        this.title = this.$route.params.title;
    },
    mounted() {
        axios
            .get(`${CONFIG.baseURL}/api/news/?format=json`, {
                params: { title: this.title }
            })
            .then(response => {
                let events = [];
                events = response.data;
                this.events = Object.assign({}, this.events, events);
            });
    }
};
</script>
