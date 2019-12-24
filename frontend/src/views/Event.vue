<template>
    <div class="event pt-40 md:pt-60 flex flex-col ml-8 mr-8 md:ml-0 md:mr-0">
        <div class="flex flex-col pb-40">
            <div class="flex flex-col md:flex-row">
                <div class="flex flex-col md:ml-60">
                    <router-link to="/news"
                        ><div><img src="@/assets/images/back.svg" /></div
                    ></router-link>
                    <div class="mt-24 md:mt-32">
                        {{event}}
                    </div>
                    <div
                        class="md:w-feed mt-20 font-black text-3xl leading-180"
                    >
                        SYNTAX ERROR - CAMPUS HACKATHON
                    </div>
                    <div class="mt-8 text-base font-semibold leading-170">
                        27 - 30th September, 2018
                    </div>
                    <div class="md:w-feed mt-14 text-base leading-normal">
                        Lorem ipsum dolor sit amet, consectetuer adipiscing
                        elit. Aenean commodo ligula eget dolor. Lorem ipsum
                        dolor sit amet, consectetuer adipiscing elit.
                    </div>
                    <div class="mt-28">
                        <Button
                            v-bind:native="true"
                            url="https://hackathon.sdslabs.co/"
                            text="Register Now"
                        />
                    </div>
                </div>
                <div class="mt-20 md:mt-0 md:ml-44 shadow-image">
                    <img
                        class="md:w-image"
                        src="https://s3-alpha-sig.figma.com/img/d38b/3f21/a3050d8d31199a8546e856facd804c3e?Expires=1578268800&Signature=ItJ7NgQ8ECd6vLYpJFm8Bnpmy8Lyg~G5CEWW2TtG9lY-FxGxsWDbdSyQkmORnUemF-GS99Kr2ouhH42aCWRKtMWWPBNJ7R5iQQDCpL~uhoUgXt5R4C3xC-h0BXdUd4jhVoo2XI0UXxqZlhfXJN0LRnRAF2z8VNyd~Ogm110p~RM3WaQbOk0d2kk-MWlwvu9kiqKxyHJJhyc6CK1JUyN6G07SAupqxdvSoc0f-0aw9~eD1z1EqDL65uFv95xx4mqsIYDnfR1e~uXqwT59sKwa5ludZUsWv2yQhSbLSroc-cNylDO~6wO1BxNpWYWZtBIqHgeX2nKHqCXsX7JN8TqbVA__&Key-Pair-Id=APKAINTVSUGEWH5XD5UA"
                    />
                </div>
            </div>
            <div class="md:ml-60 mt-40 text-base md:w-eventdesc leading-normal">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean
                ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl.
                Pellentesque sagittis fringilla tempor. Pellentesque sit amet
                augue sit amet quam feugiat porta vitae sit amet ligula. Nulla
                posuere pellentesque metus sit amet posuere. Suspendisse
                potenti. Nullam nulla quam, imperdiet vel felis lobortis, tempor
                pellentesque libero. Curabitur et fermentum sapien. In hac
                habitasse platea dictumst. Sed nec semper ligula, scelerisque
                porttitor dui. Quisque congue, diam eu euismod rutrum, ex metus
                ultricies odio, eu consequat enim elit sed elit. Fusce vehicula
                sapien convallis nisl venenatis interdum. Nullam id vulputate
                dolor. Aenean sagittis vestibulum laoreet. Nulla pulvinar
                feugiat nisl eget egestas. Aliquam dapibus euismod ipsum, in
                rhoncus elit. Cras eu luctus sem, et volutpat nulla. Cras sed
                pretium turpis. Pellentesque rhoncus risus vitae metus efficitur
                vulputate. Aenean ante tortor, dictum ut arcu eget, finibus
                ullamcorper justo. Donec pellentesque pharetra quam, vitae
                convallis ante faucibus vitae. Integer mollis, enim tincidunt
                blandit commodo, lectus libero convallis odio, in condimentum
                nibh erat in libero. Nunc sagittis vitae nulla non.
            </div>
        </div>
        <div class="flex flex-col">
            <div class="mt-40 md:ml-60 font-extrabold text-lg leading-170">
                2 Updates
            </div>
            <div>
                <Update
                    title="ANSWERING YOUR QUESTIONS"
                    date=""
                    timing="28th September, 2018 | 7:00 PM | LHC 005"
                    description1="You can join the facebook group: https://www.facebook.com/groups/198447694257165/ to connect with different year's students specially 1st year students with lots of amazing skills. Regarding topic you can make anything you like."
                    description2="Register fast and remember hackathons are purely for learning and yeah of course prizes and free food! :P"
                    description3="Happy coding!"
                    url="error.svg"
                />
            </div>
            <Update
                title="ANSWERING YOUR QUESTIONS"
                date=""
                description="As many of you have similar questions regarding teams and topics, we decided to come up with this post."
                description1="You can join the facebook group: https://www.facebook.com/groups/198447694257165/ to connect with different year's students specially 1st year students with lots of amazing skills. Regarding topic you can make anything you like."
                description2="Register fast and remember hackathons are purely for learning and yeah of course prizes and free food! :P"
                description3="Happy coding!"
                url=""
            />
        </div>
    </div>
</template>

<script>
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
    props: {
        event: Object,
        eventUpdates: Array
    }
};
</script>
