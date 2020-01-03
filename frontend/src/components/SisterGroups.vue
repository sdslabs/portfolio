<template>
    <div
        class="sister-groups w-auto flex flex-col sm:content-center ml-8 mr-8 sm:ml-0 sm:mr-0 sm:pt-60"
    >
        <div
            class="text-3xl font-extrabold sm:self-center leading-loose sm:w-feed sm:text-center"
        >
            Sister Groups
        </div>
        <div
            class="sm:w-180 pt-6 text-lg text-grey leading-170 sm:self-center sm:text-center sm:w-sister"
        >
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac
            lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque
            sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam
            feugiat porta vitae sit amet ligula.
        </div>
        <div
            class="sister flex flex-row self-center mt-32 justify-between sm:w-groups"
        >
            <div>
                <Sister
                    v-bind:url="dsg"
                    title="DATA SCIENCE GROUP"
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."
                />
            </div>
            <div>
                <Sister
                    class="ml-10"
                    v-bind:url="pag"
                    title="PROGRAMMING & ALGORITHMS GROUP"
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."
                />
            </div>
            <div>
                <Sister
                    class="ml-10"
                    v-bind:url="infosec"
                    title="INFOSEC IITR"
                    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."
                />
            </div>
        </div>
        <div class="mt-12 sm:hidden"><SisterGallery /></div>
    </div>
</template>

<script>
import Sister from "@/components/about/Sister.vue";
import SisterGallery from "@/components/about/SisterGallery.vue";
import dsg from "@/assets/images/dsg.svg";
import pag from "@/assets/images/pag.svg";
import infosec from "@/assets/images/infosec.svg";
export default {
    name: "SisterGroups",
    components: {
        Sister,
        SisterGallery
    },
    data: function initData() {
        return {
            dsg: dsg,
            pag: pag,
            infosec: infosec
        };
    }
};
</script>

<style lang="scss" scoped>
@media screen and (max-width: 576px) {
    .sister {
        display: none;
    }
}
</style>
