import React from "react";

function WarnningBanner(props) {
    if (!props.warning) {
        return null;
    }

    return (
        <div>경고!</div>
    );
}

export default WarnningBanner;