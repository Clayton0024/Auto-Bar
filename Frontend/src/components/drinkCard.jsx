import * as React from "react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function DrinkCard({ titleText, descriptionText, imgSrc, imgAlt }) {
  return (
    <Card
      className="w-100 border-primary"
      onClick={() => {
        console.log("clicked drink");
      }}
    >
      <CardHeader>
        <CardTitle>{titleText}</CardTitle>
        <CardDescription>{descriptionText}</CardDescription>
      </CardHeader>
      <CardContent>
        <img src={imgSrc} alt={imgAlt} />
      </CardContent>
      <CardFooter className="flex justify-end"></CardFooter>
    </Card>
  );
}
