<template>
    <div class="event pt-40 md:pt-60 flex flex-col ml-8 mr-8 md:ml-0 md:mr-0">
        <div class="flex flex-col pb-40">
            <div class="flex flex-col md:flex-row">
                <div class="flex flex-col md:ml-60">
                    <router-link to="/news"
                        ><div><img src="@/assets/images/back.svg" /></div
                    ></router-link>
                    <div class="mt-24 md:mt-32">
                        {{ event.types.toUpperCase() }}
                    </div>
                    <div
                        class="md:w-feed mt-20 font-black text-3xl leading-180"
                    >
                        {{ event.title.toUpperCase() }}
                    </div>
                    <div class="mt-8 text-base font-semibold leading-170">
                        {{ event.timing }}
                    </div>
                    <div class="md:w-feed mt-14 text-base leading-normal">
                        {{ event.description }}
                    </div>
                    <div class="mt-28">
                        <Button
                            v-bind:native="true"
                            :url="event.url"
                            text="Register Now"
                        />
                    </div>
                </div>
                <div class="mt-20 md:mt-0 md:ml-44 shadow-image">
                    <img
                        class="md:w-image"
                        :src="event.image"
                    />
                </div>
            </div>
            <div class="md:ml-60 mt-40 text-base md:w-eventdesc leading-normal">
                {{ event.description1 }}
            </div>
        </div>
        <div class="flex flex-col" v-if="event.event_update.length != 0">
            <div class="mt-40 md:ml-60 font-extrabold text-lg leading-170">
                {{ event.event_update.length }} Updates
            </div>
            <div>
                <Update
                    :title="event.event_update.title"
                    date="" 
                    :timing="event.event_update.timing"
                    :description1="event.event_update.description1"
                    :description2="event.event_update.description2"
                    :description3="event.event_update.description3"
                    :url="event.event_update.url"
                />
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Label from "@/components/Label.vue";
import Update from "@/components/Update.vue";
import Button from "@/components/Button.vue";
export default {
    name: "event",
    components: {
        Label,
        Button,
        Update
    },
    data () {
        return {
            title: "",
        }
    },
    created() {
        this.title = this.$route.params.title;
    },
    mounted() {
        axios
            .get("http://0.0.0.0:8000/api/news/?format=json", {
                params: {
                    title: title
                }
            })
            .then(response => {
                let event = {}
                event = response.data
                this.event = Object.assign({}, this.event, event);
            });
    }
};
</script>
