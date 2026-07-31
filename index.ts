#!/usr/bin/env node

interface MindProfileInput {
  student: string;
  gradeLevel: string;
  studentProfile: number;
  careerReadiness: number;
  learningStyle: number;
  psychometric: number;
  multipleIntelligence: number;
  streamReadiness: number;
}

interface MindProfileOutput {
  student: string;
  gradeLevel: string;
  studentProfileScore: number;
  careerReadinessScore: number;
  learningStyleScore: number;
  psychometricScore: number;
  multipleIntelligenceScore: number;
  streamReadinessScore: number;
  overallMindProfileIndex: number;
  priorityAction: string;
  recommendedPathways: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    studentProfile: "Student Profile",
    careerReadiness: "Career Readiness",
    learningStyle: "Learning Style",
    psychometric: "Psychometric",
    multipleIntelligence: "Multiple Intelligence",
    streamReadiness: "Stream Readiness",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getRecommendedPathways(mi: number, career: number, stream: number): Record<string, number> {
  return {
    "Engineering & Technology": Math.min(100, Math.round(mi * 1.05)),
    "Medicine & Healthcare": Math.min(100, Math.round(career * 1.0)),
    "Business & Management": Math.min(100, Math.round(stream * 1.1)),
    "Arts & Humanities": Math.min(100, Math.round(mi * 0.94)),
  };
}

export function analyzeMindProfile(input: MindProfileInput): MindProfileOutput {
  const scores = {
    studentProfile: input.studentProfile,
    careerReadiness: input.careerReadiness,
    learningStyle: input.learningStyle,
    psychometric: input.psychometric,
    multipleIntelligence: input.multipleIntelligence,
    streamReadiness: input.streamReadiness,
  };
  const overallMindProfileIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    student: input.student,
    gradeLevel: input.gradeLevel,
    studentProfileScore: input.studentProfile,
    careerReadinessScore: input.careerReadiness,
    learningStyleScore: input.learningStyle,
    psychometricScore: input.psychometric,
    multipleIntelligenceScore: input.multipleIntelligence,
    streamReadinessScore: input.streamReadiness,
    overallMindProfileIndex,
    priorityAction: getPriorityAction(scores),
    recommendedPathways: getRecommendedPathways(input.multipleIntelligence, input.careerReadiness, input.streamReadiness),
  };
}

const args = process.argv.slice(2);
const student = args[0] || "student-profile";
const gradeLevel = args[1] || "Grade-12";
const studentProfile = parseInt(args[2]) || 85;
const careerReadiness = parseInt(args[3]) || 82;
const learningStyle = parseInt(args[4]) || 88;
const psychometric = parseInt(args[5]) || 78;
const multipleIntelligence = parseInt(args[6]) || 90;
const streamReadiness = parseInt(args[7]) || 80;

const result = analyzeMindProfile({
  student, gradeLevel, studentProfile, careerReadiness,
  learningStyle, psychometric, multipleIntelligence, streamReadiness,
});

console.log(`Student: ${result.student}`);
console.log(`Grade Level: ${result.gradeLevel}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Student Profile Score:         ${result.studentProfileScore}/100  [${getStatus(result.studentProfileScore)}]`);
console.log(`Career Readiness Score:        ${result.careerReadinessScore}/100  [${getStatus(result.careerReadinessScore)}]`);
console.log(`Learning Style Score:          ${result.learningStyleScore}/100  [${getStatus(result.learningStyleScore)}]`);
console.log(`Psychometric Score:            ${result.psychometricScore}/100  [${getStatus(result.psychometricScore)}]`);
console.log(`Multiple Intelligence Score:   ${result.multipleIntelligenceScore}/100  [${getStatus(result.multipleIntelligenceScore)}]`);
console.log(`Stream Readiness Score:        ${result.streamReadinessScore}/100  [${getStatus(result.streamReadinessScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Mind Profile Index:    ${result.overallMindProfileIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nRecommended Career Pathways:");
Object.entries(result.recommendedPathways).forEach(([pathway, score]) => {
  console.log(`  ${pathway.padEnd(28)} ${score}/100`);
});
