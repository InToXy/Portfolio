import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import ProjectCard from "./ProjectCards";
import Particle from "../Particle";
import pentestImg from "../../Assets/pentest.jpg";
import dataImg from "../../Assets/data.jpeg";
import cloudImg from "../../Assets/cloud.jpeg";
import infraImg from "../../Assets/hacker-1944688_1920.jpg";

function Projects() {
  return (
    <Container fluid className="project-section">
      <Particle />
      <Container>
        <h1 className="project-heading">
          My Recent <strong className="purple">Works </strong>
        </h1>
        <p style={{ color: "white" }}>
          Here are a few projects I've worked on recently.
        </p>
        <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>
          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={pentestImg}
              isBlog={false}
              title="Introduction au Pentesting"
              description="Apprentissage de differents type de scan de vulnerabilité et utilisation de scripts afin de les exploiters."
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={dataImg}
              isBlog={false}
              title="Traitement de données"
              description="Création d'un code python pour traiter et mettre en forme un fichier CVE du planning de l'année scolaire."
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={cloudImg}
              isBlog={false}
              title="Réseau informatique Cloud"
              description="Mise en place d’un réseau informatique Cloud avec la configuration de différents services sur des machines Centos8."
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={infraImg}
              isBlog={false}
              title="Assurer la sécurisation d'un SI"
              description="Implémentation complète d'une infrastructure réseau de A à Z incluant sa sécurisation."
            />
          </Col>
        </Row>
      </Container>
    </Container>
  );
}

export default Projects;
