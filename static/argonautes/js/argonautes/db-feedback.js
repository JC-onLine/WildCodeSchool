window.addEventListener("load", function(){
    const log = false;
    let wamp_url
    // Get hostname from DJANGO_URL
    const hostname = DJANGO_URL;
    console.log("DJANGO_URL:" + DJANGO_URL)
    if (hostname === "127.0.0.1") {
        wamp_url = 'ws://' + hostname + ':8080/ws';
    } else {
        wamp_url = "wss://" + hostname + "/ws";
    }
    /* Connection configuration to our WAMP router */
    var connection = new autobahn.Connection({
        // default url= url: 'ws://127.0.0.1:8080/ws',
        url: wamp_url,
        realm: 'realm1'
    });
    if (log===true) { console.log("db-feedback.js: Autobahn definition with: " + wamp_url) };

    // Connection opened
    // let team_list_json_cp;
    connection.onopen = function(session) {
        console.log("db-feedback.js: Autobahn ws connected!");

        // ==== TOPIC CHANNEL ====
        //When we receive the 'client_topic' event, CLEAR/DISPLAY the page
        session.subscribe('argonautes_channel', function(args){
            console.log("db-feedback.js: --> client subscribed on argonautes_channel!");
            // get team_list_json from python autobahn websocket
            let team_list_json = args[0];
            if (log===true) { console.log("db-feedback.js: team_list_json.topic=" + team_list_json.topic)};
            if (team_list_json.topic !== "") {
                if (log===true) { console.log("db-feedback.js: start remove div_container...")};
                let node_container;
                node_container = document.getElementById("div_container");
                // remove node_container
                if (node_container) {
                    node_container.remove();
                    if (log===true) { console.log("db-feedback.js: 'div_container' removed.")};

                    if (log===true) { console.log("db-feedback.js: starting create 'div_container'...")};
                    let section = document.getElementById("team-list-section");
                    let div_container_new = document.createElement("div");
                    div_container_new.id = 'div_container';
                    div_container_new.setAttribute("class", "div_container");
                    if (log===true) { console.log("db-feedback.js: 'div_container_new' " + div_container_new)};

                    // draw column 1 in DOM
                    draw_column(div_container_new, team_list_json.topic.column1, log);
                    draw_column(div_container_new, team_list_json.topic.column2, log);
                    draw_column(div_container_new, team_list_json.topic.column3, log);
                    section.appendChild(div_container_new);
                    console.log("db-feedback.js: DOM create done.");
                }else{
                    console.log("db-feedback.js: 'div_container' not found.");
                }
            }
        }); //subscribe
    } //onopen
    // Open the WAMP connection with the router.
    connection.open();
}); //addEventListener
