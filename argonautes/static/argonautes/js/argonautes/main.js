window.addEventListener("load", function(){
    const log = true;
    let wamp_url
    let node_container;
    // Get hostname from DJANGO_URL
    const hostname = DJANGO_URL;
    console.log("DJANGO_URL:" + DJANGO_URL)
    // Wamp url https adaptation
    if (hostname === "127.0.0.1") {
        wamp_url = 'ws://' + hostname + ':8080/ws';
    } else {
        wamp_url = "wss://" + hostname + "/ws";
    }

    /* ==== Display this page on boot ==== */
    if (log===true) { console.log("main.js: starting create 'div_container'...")}
    let section = document.getElementById("team-list-section");
    let div_container_new = document.createElement("div");
    div_container_new.id = 'div_container';
    div_container_new.setAttribute("class", "div_container");
    if (log===true) { console.log(
        "main.js: 'team_list_on_first_open.topic' " + boot_page_db.topic
    )}
    // draw column 1,2 and 3 in DOM
    draw_column(1, div_container_new, boot_page_db.topic.column1, log);
    draw_column(2, div_container_new, boot_page_db.topic.column2, log);
    draw_column(3, div_container_new, boot_page_db.topic.column3, log);
    section.appendChild(div_container_new);
    console.log("main.js: DOM create done.");

    /* ==== Connection configuration to our WAMP router ==== */
    let connection = new autobahn.Connection({
        // default url= url: 'ws://127.0.0.1:8080/ws',
        url: wamp_url,
        realm: 'realm1'
    });
    if (log===true) { console.log("main.js: Autobahn definition with: " + wamp_url) }

    // Connection opened
    // let team_list_json_cp;
    connection.onopen = function(session) {
        console.log("main.js: Autobahn ws connected!");

        // ==== TOPIC CHANNEL ====
        //When we receive the 'client_topic' event, CLEAR/DISPLAY the page
        session.subscribe('argonautes_channel', function(args){
            console.log("main.js: --> client subscribed on argonautes_channel!");
            // get team_list_json from python autobahn websocket
            let team_list_json = args[0];
            if (log===true) { console.log("main.js: team_list_json.topic=" + team_list_json.topic)}
            if (team_list_json.topic !== "") {
                if (log===true) { console.log("main.js: boot_page_db = null")}
                boot_page_db = null;
                if (log===true) { console.log("main.js: start remove div_container...")}
                node_container = document.getElementById("div_container");
                // remove node_container
                if (node_container) {
                    node_container.remove();
                    if (log===true) { console.log("main.js: 'div_container' removed.")}

                    if (log===true) { console.log("main.js: starting create 'div_container'...")}
                    let section = document.getElementById("team-list-section");
                    let div_container_new = document.createElement("div");
                    div_container_new.id = 'div_container';
                    div_container_new.setAttribute("class", "div_container");
                    if (log===true) { console.log("main.js: 'div_container_new' " + div_container_new)}

                    // draw column 1,2 and in DOM
                    draw_column(1, div_container_new, team_list_json.topic.column1, log);
                    draw_column(2, div_container_new, team_list_json.topic.column2, log);
                    draw_column(3, div_container_new, team_list_json.topic.column3, log);
                    section.appendChild(div_container_new);
                    console.log("main.js: DOM create done.");
                }else{
                    console.log("main.js: 'node_container' not found.");
                }
            }
        }); //subscribe
    } //onopen
    // Open the WAMP connection with the router.
    connection.open();
}); //addEventListener
