import React from "react";
import Typewriter from "typewriter-effect";

function Type() {
  return (
    <Typewriter
      options={{
        strings: [
          "Étudiant en Réseaux et Télécommunication",
          "Technicien Réseaux",
          "Spécialiste en Cybersécurité",
          "Administrateur Systèmes et Réseaux",
        ],
        autoStart: true,
        loop: true,
        deleteSpeed: 50,
      }}
    />
  );
}

export default Type;
