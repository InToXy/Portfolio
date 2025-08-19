import React, { useState, useEffect } from "react";
import { Container, Row, Col } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Particle from "../Particle";
import pdf from "../../Assets/CV_Matheo_Pinget_2024.pdf";
import { AiOutlineDownload } from "react-icons/ai";
import { Document, Page, pdfjs } from "react-pdf";
import "react-pdf/dist/esm/Page/AnnotationLayer.css";
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

function ResumeNew() {
  const [width, setWidth] = useState(1200);

  useEffect(() => {
    setWidth(window.innerWidth);
  }, []);

  return (
    <div>
      <Container fluid className="resume-section">
        <Particle />
        <Row className="skill-section" style={{ justifyContent: "center", paddingBottom: "50px" }}>
          <Col md={10}>
            <h1 className="project-heading">
              Professional <strong className="purple">Skillset </strong>
            </h1>
            <Row style={{ justifyContent: "center", paddingBottom: "20px" }}>
                <Col md={4}>
                    <h5 style={{color: "white"}}>Réseaux</h5>
                    <ul style={{color: "white", textAlign: "left"}}>
                        <li>Administration (Linux/Windows)</li>
                        <li>Configuration (Cisco, WatchGuard)</li>
                        <li>Protocoles (VLAN, OSPF, BGP)</li>
                        <li>Virtualisation (VMware, Proxmox)</li>
                    </ul>
                </Col>
                <Col md={4}>
                    <h5 style={{color: "white"}}>Cybersécurité</h5>
                    <ul style={{color: "white", textAlign: "left"}}>
                        <li>Analyse de vulnérabilités</li>
                        <li>Pentesting</li>
                        <li>Sécurisation des SI</li>
                        <li>Cryptographie & PKI</li>
                    </ul>
                </Col>
                <Col md={4}>
                    <h5 style={{color: "white"}}>Développement</h5>
                    <ul style={{color: "white", textAlign: "left"}}>
                        <li>Python (Scripting, API REST)</li>
                        <li>Java (Applications, JavaFX)</li>
                        <li>Scripting (Bash, Powershell)</li>
                        <li>CI/CD & DevOps (Docker, Ansible)</li>
                    </ul>
                </Col>
            </Row>
          </Col>
        </Row>
        <Row style={{ justifyContent: "center", position: "relative" }}>
          <Button
            variant="primary"
            href={pdf}
            target="_blank"
            style={{ maxWidth: "250px" }}
          >
            <AiOutlineDownload />
            &nbsp;Download CV
          </Button>
        </Row>

        <Row className="resume">
          <Document file={pdf} className="d-flex justify-content-center">
            <Page pageNumber={1} scale={width > 786 ? 1.7 : 0.6} />
          </Document>
        </Row>

        <Row style={{ justifyContent: "center", position: "relative" }}>
          <Button
            variant="primary"
            href={pdf}
            target="_blank"
            style={{ maxWidth: "250px" }}
          >
            <AiOutlineDownload />
            &nbsp;Download CV
          </Button>
        </Row>
      </Container>
    </div>
  );
}

export default ResumeNew;
