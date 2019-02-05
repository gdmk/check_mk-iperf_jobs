metric_info["bw_from"] = {
    "title" : _("bandwidth from the Host"),
    "unit"  : "bits/s",
    "color" : "#00e060",
}

metric_info["bw_to"] = {
    "title" : _("bandwidth to the Host"),
    "unit"  : "bits/s",
    "color" : "#0080e0",
}

graph_info["Iperf_bandwidth"] = {
    "title" : _("Iperf Bandwidth"),
    "metrics" : [
        ( "bw_from",   "area", ),
        ( "bw_to",  "-area", ),
    ],
    "scalars": [
        ("bw_from:warn", "Warning from"),
        ("bw_from:crit", "Critical from"),
        ("bw_to:warn,-1,*", "Warning to"),
        ("bw_to:crit,-1,*", "Critical to"),
    ]
}



metric_info["pkt_lost_from"] = {
    "title" : _("Lost Packets from the Host"),
    "unit"  : "count",
    "color" : "11/a",
}

metric_info["pkt_lost_to"] = {
    "title" : _("Lost Packets to the Host"),
    "unit"  : "count",
    "color" : "15/a",
}

graph_info["packets_lost"] = {
    "title" : _("Iperf Lost Packets"),
    "metrics" : [
        ( "pkt_lost_from",  "area" ),
        ( "pkt_lost_to", "-area" ),
    ],
    "scalars": [
        ("pkt_lost_from:warn", "Warning from"),
        ("pkt_lost_from:crit", "Critical from"),
        ("pkt_lost_to:warn,-1,*", "Warning to"),
        ("pkt_lost_to:crit,-1,*", "Critical to"),
    ]
}

metric_info["prct_lost_from"] = {
        "title" : _("Percent of Lost Packets from the Host"),
        "unit"  : "%",
        "color" : "11/c",
}

metric_info["prct_lost_to"] = {
        "title" : _("Percent of Lost Packets to the Host"),
        "unit"  : "%",
        "color" : "15/c",
}

graph_info["packets_lost_prct"] = {
    "title" : _("Iperf Percent of Lost Packets"),
    "metrics" : [
        ("prct_lost_from", "area"),
	("prct_lost_to", "-area"),
    ],
    "scalars": [
        ("prct_lost_from:warn", "Warning from"),
        ("prct_lost_from:crit", "Critical from"),
        ("prct_lost_to:warn,-1,*", "Warning to"),
        ("prct_lost_to:crit,-1,*", "Critical to"),
    ]
}


metric_info["jitter_from"] = {
        "title" : _("Jitter from the Host"),
        "unit"  : "s",
        "color" : "36/a",
}

metric_info["jitter_to"] = {
        "title" : _("Jitter to the Host"),
        "unit"  : "s",
        "color" : "34/b",
}

graph_info["packet_jitter"] = {
    "title" : _("Iperf Jitter"),
    "metrics" : [
        ("jitter_from", "area"),
        ("jitter_to", "-area"),
    ],
    "scalars": [
        ("jitter_from:warn", "Warning from"),
        ("jitter_from:crit", "Critical from"),
        ("jitter_to:warn,-1,*", "Warning to"),
        ("jitter_to:crit,-1,*", "Critical to"),
    ]
}


metric_info["retr_from"] = {
    "title" : _("TCP retransmits from the Host"),
    "unit"  : "count",
    "color" : "44/a",
}

metric_info["retr_to"] = {
    "title" : _("TCP retransmits to the Host"),
    "unit"  : "count",
    "color" : "34/a",
}

graph_info["retransmits"] = {
    "title" : _("Iperf TCP Retransmits"),
    "metrics" : [
        ( "retr_from",  "area" ),
        ( "retr_to", "-area" ),
    ],
    "scalars": [
        ("retr_from:warn", "Warning from"),
        ("retr_from:crit", "Critical from"),
        ("retr_to:warn,-1,*", "Warning to"),
        ("retr_to:crit,-1,*", "Critical to"),
    ]
}

