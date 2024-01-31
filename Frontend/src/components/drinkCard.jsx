import * as React from "react";
import { useState } from "react";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { DrinkDialog } from "./drinkDialog";

export function DrinkCard({ titleText, descriptionText, imgSrc, imgAlt, id }) {
  const [showDialog, setShowDialog] = useState(false);

  function dialogCleanUp() {
    setShowDialog(false);
  }

  return (
    <>
      {showDialog && (
        <DrinkDialog
          id={id}
          title={titleText}
          onClose={() => dialogCleanUp()}
        />
      )}
      <Card
        className="w-100"
        onClick={() => {
          setShowDialog(true);
        }}
      >
        <CardHeader>
          <CardTitle>{titleText}</CardTitle>
          {descriptionText && (
            <CardDescription>{descriptionText}</CardDescription>
          )}
        </CardHeader>
        <CardContent>
          <img src={imgSrc} alt={imgAlt} className="rounded-md" />
        </CardContent>
        <CardFooter className="flex justify-end"></CardFooter>
      </Card>
    </>
  );
}
