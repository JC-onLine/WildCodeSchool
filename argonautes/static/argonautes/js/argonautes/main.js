window.addEventListener("load", function(){
    /* Install Websocket listener
    Data from Django:
    - DJANGO_URL  : Use to link Websockets to the server.
    - app_settings: Aplication settings like:
                    - members_maxi  : Maxi of team members list.
                    - columns_number: Number of columns in the web rendering page.
    - page_boot_db: Members list on first diplay page from Django.
    */
    const log = true;
    let wamp_url
    let node_container;
    // Get hostname from DJANGO_URL
    const hostname = DJANGO_URL;
    console.log("DJANGO_URL:" + DJANGO_URL)
    // Page design
    // let design_setup = {
    //     members_maxi: app_settings.members_maxi,
    //     columns_number: app_settings.columns_number,
    // }
    // Wamp url https adaptation
    if (hostname === "127.0.0.1") {
        wamp_url = 'ws://' + hostname + ':8080/ws';
    } else {
        wamp_url = "wss://" + hostname + "/ws";
    }

    /* ==== Display members colums on boot ==== */
    if (log===true) { console.log("main.js: starting create 'list_member_container'...")}
    // refresh total count
    document.getElementById("total-count").textContent = calcul_total(page_boot_db);
    let section = document.getElementById("team-list-section");
    let list_member_container_new = document.createElement("div");
    list_member_container_new.id = 'list_member_container';
    list_member_container_new.setAttribute("class", "list_member_container");
    if (log===true) {
        console.log("main.js: app_settings.members_maxi " + app_settings.members_maxi);
        console.log("main.js: app_settings.columns_number " + app_settings.columns_number);
    }
    // draw column 1,2 and in DOM
    draw_colums("list_member_container", page_boot_db, app_settings, true);
                    // let members_total_count = calcul_total(page_boot_db)
                    // document.getElementById("total-count").textContent = members_total_count;
                    // // disable input form if members > maxi
                    // if (members_total_count >= app_settings.members_maxi) {
                    //     document.getElementById("send-button").
                    //         setAttribute("disabled", "disabled");
                    //     document.getElementById("name").
                    //         setAttribute("disabled", "disabled");
                    //     document.getElementById("name").placeholder = " C'est complet !";
                    //     document.getElementById("name").className = "full";
                    // }
                    // draw_column(1, list_member_container_new, page_boot_db.column1, log);
                    // draw_column(2, list_member_container_new, page_boot_db.column2, log);
                    // draw_column(3, list_member_container_new, page_boot_db.column3, log);
                    // section.appendChild(list_member_container_new);
                    // console.log("main.js: DOM create done.");

    /* ==== Connection configuration to our WAMP router ==== */
    let connection = new autobahn.Connection({
        // default url= url: 'ws://127.0.0.1:8080/ws',
        url: wamp_url,
        realm: 'realm1'
    });
    if (log===true) { console.log("main.js: Autobahn definition with: " + wamp_url) }

    // Connection opened
    connection.onopen = function(session) {
        console.log("main.js: Autobahn ws connected!");

        // ==== RUNTIME CHANNEL ====
        //When we receive the 'client_topic' event, CLEAR/DISPLAY the page columns.
        session.subscribe('argonautes_channel', function(args){
            console.log("main.js: --> client subscribed on argonautes_channel!");
            // get team_list_json from python autobahn websocket
            let team_list_json = args[0];
            if (team_list_json !== "") {
                if (log===true) { console.log("main.js: team_list_json.column1=" + team_list_json.column1)}
                if (log===true) { console.log("main.js: page_boot_db = null")}
                page_boot_db = null;
                if (log===true) { console.log("main.js: start remove list_member_container...")}
                node_container = document.getElementById("list_member_container");
                // remove node_container
                if (node_container) {
                    node_container.remove();
                    if (log===true) { console.log("main.js: 'list_member_container' removed.")}

                    if (log===true) { console.log("main.js: starting create 'list_member_container'...")}
                    let section = document.getElementById("team-list-section");
                    let list_member_container_new = document.createElement("div");
                    list_member_container_new.id = 'list_member_container';
                    list_member_container_new.setAttribute("class", "list_member_container");
                    if (log===true) { console.log("main.js: 'list_member_container_new' " + list_member_container_new)}

                    // draw column 1,2 and in DOM
                    let members_total_count = calcul_total(team_list_json)
                    document.getElementById("total-count").textContent = members_total_count;
                    // disable input form if members > maxi
                    if (members_total_count >= app_settings.members_maxi) {
                        document.getElementById("send-button").
                            setAttribute("disabled", "disabled");
                        document.getElementById("name").
                            setAttribute("disabled", "disabled");
                        document.getElementById("name").placeholder = " C'est complet !";
                        document.getElementById("name").className = "full";
                    }
                    draw_column(1, list_member_container_new, team_list_json.column1, log);
                    draw_column(2, list_member_container_new, team_list_json.column2, log);
                    draw_column(3, list_member_container_new, team_list_json.column3, log);
                    section.appendChild(list_member_container_new);
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
