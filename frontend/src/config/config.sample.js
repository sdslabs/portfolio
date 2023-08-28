export const config = {
    client: {
        id: "",
        secret: ""
    },
    auth: {
        tokenHost: "http://falcon.sdslabs.local",
        tokenPath: "http://falcon.sdslabs.local/access_token",
        authorizePath: "http://falcon.sdslabs.local/authorize"
    },
    scopes: ["email", "image_url", "organizations"],
    user: {
        url_resource_owner_details: "http://falcon.sdslabs.local/users",
        redirect_url: "",
        accounts_url: "http://arceus.sdslabs.local"
    }
};
