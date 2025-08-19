import React from "react";
import Card from "react-bootstrap/Card";
import { ImPointRight } from "react-icons/im";

function AboutCard() {
  return (
    <Card className="quote-card-view">
      <Card.Body>
        <blockquote className="blockquote mb-0">
          <p style={{ textAlign: "justify" }}>
            En tant que <span className="purple">Technicien Entreprise</span> chez <span className="purple">Orange</span>, j'ai développé une expertise solide dans un environnement stimulant et innovant.
            <br />
            Mon rôle au sein de l'Unité d'Intervention Auvergne-Rhône-Alpes à Annemasse m'a permis de maîtriser plusieurs aspects clés du métier.
            <br />
            <br />
            Mes responsabilités principales incluent :
          </p>
          <ul>
            <li className="about-activity">
              <ImPointRight /> <strong>Production et Installation :</strong> Mise en place d'équipements de télécommunications chez les clients.
            </li>
            <li className="about-activity">
              <ImPointRight /> <strong>Dépannage et Maintenance :</strong> Diagnostic et résolution de pannes sur le réseau.
            </li>
            <li className="about-activity">
              <ImPointRight /> <strong>Communication Client :</strong> Assurer un service de qualité et une communication claire.
            </li>
          </ul>
          <p style={{ textAlign: "justify" }}>
            J'ai également eu l'opportunité de travailler sur des projets techniques comme la technologie <span className="purple">MD2G</span>, une solution de liaison privée sécurisée pour des clients majeurs, renforçant ainsi mes compétences en réseaux et sécurité.
          </p>
        </blockquote>
      </Card.Body>
    </Card>
  );
}

export default AboutCard;
